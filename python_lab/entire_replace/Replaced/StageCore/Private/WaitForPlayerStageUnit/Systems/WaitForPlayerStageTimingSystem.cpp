// Fill out your copyright notice in the Description page of Project Settings.

#include "StageCore.h"
#include "WaitForPlayerStageTimingSystem.h"
#include "DeviceActionMessage.h"
#include "TSMHand.h"
#include "TSMWorldConfig.h"
#include "DeviceControlState.h"
#include "GlobalRequestPath.h"

#include "Message.h"
#include "SystemMessagePath.h"
#include "TSMApp.h"

#include "GameStageManager/GameStageManager.h"

#include "../Utils/WaitForPlayerStageUnitReq.h"

#include "../Session/WaitForPlayerStageUnitSession.h"



AWaitForPlayerStageTimingSystem::AWaitForPlayerStageTimingSystem()
{
	PrimaryActorTick.bCanEverTick = true;
}

void AWaitForPlayerStageTimingSystem::Tick(float DeltaSeconds)
{
	OnTickUpdateRemainingTime(DeltaSeconds);
	OnTickDebugRemainingTime();
}

FString AWaitForPlayerStageTimingSystem::GetHandlePath() const
{
	return WaitForPlayerStageUnitReq::WaitForPlayerStageStartCountDown::Path();
}

void AWaitForPlayerStageTimingSystem::HandleRequest(FRequestPtr InOutRequest, FResponsePtr InOutResponse)
{
	GEngine->AddOnScreenDebugMessage(-1, 5, FColor::Red, "AWaitForPlayerStageTimingSystem", false);

	StartTiming(6);
}

void AWaitForPlayerStageTimingSystem::RegisterUnitSession()
{
	SetUnitSession(AWaitForPlayerStageUnitSession::StaticClass());
}

void AWaitForPlayerStageTimingSystem::RegisterEntityComps()
{
}

void AWaitForPlayerStageTimingSystem::RegisterRequests()
{
	RegisterRequest(GlobalRequestPath::ChangeGameStage::Path());
}

void AWaitForPlayerStageTimingSystem::OnTickUpdateRemainingTime(float DeltaSeconds)
{
	AWaitForPlayerStageUnitSession* session = GetUnitSession<AWaitForPlayerStageUnitSession>();
	if (session->GetIsTiming() == true)
	{
		RemainingTime -= DeltaSeconds;
		if (RemainingTime < 0)
		{
			OnTimingEnd();
		}
	}
}

void AWaitForPlayerStageTimingSystem::OnTimingEnd()
{
	AWaitForPlayerStageUnitSession* session = GetUnitSession<AWaitForPlayerStageUnitSession>();

	session->SetIsTiming(false);

	//if (TSMApp::Instance().GetGameStageManager().IsLocalRound())
	//{
	FRequestPtr req = FRequest::CreateRequest(GlobalRequestPath::ChangeGameStage::Path());
	req->AddParameter(
		GlobalRequestPath::ChangeGameStage::RequestParam::ToStage(),
		GameStageName::RoundBeginStage
		);
	SendRequest(req);
	//}
	//else
	//{
	//	FRequestPtr req = FRequest::CreateRequest(GlobalRequestPath::ChangeGameStage::Path());
	//	req->AddParameter(
	//		GlobalRequestPath::ChangeGameStage::RequestParam::ToStage(),
	//		GameStageName::OtherRoundBeginStage
	//		);
	//	SendRequest(req);
	//}
}

void AWaitForPlayerStageTimingSystem::OnTickDebugRemainingTime()
{
	// Songlingyi Debug
	AWaitForPlayerStageUnitSession* session = GetUnitSession<AWaitForPlayerStageUnitSession>();
	if (session->GetIsTiming() == true)
	{
		FString str = "WaitForPlayerStage RemainingTime : " + FString::SanitizeFloat(RemainingTime);
		GEngine->AddOnScreenDebugMessage(-1, 0, FColor::Green, str, false);
	}
}

void AWaitForPlayerStageTimingSystem::StartTiming(float InRemainingTime)
{
	// 1. set is timing in session
	AWaitForPlayerStageUnitSession* session = GetUnitSession<AWaitForPlayerStageUnitSession>();
	session->SetIsTiming(true);

	// 2. set RemainingTime
	RemainingTime = InRemainingTime;
}


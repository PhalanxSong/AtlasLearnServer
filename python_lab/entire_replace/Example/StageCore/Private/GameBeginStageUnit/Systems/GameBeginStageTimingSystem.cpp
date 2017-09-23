// Fill out your copyright notice in the Description page of Project Settings.

#include "StageCore.h"
#include "GameBeginStageTimingSystem.h"
#include "DeviceActionMessage.h"
#include "TSMHand.h"
#include "TSMWorldConfig.h"
#include "DeviceControlState.h"
#include "GlobalRequestPath.h"

#include "Message.h"
#include "SystemMessagePath.h"
#include "TSMApp.h"

#include "GameStageManager/GameStageManager.h"

#include "../Utils/GameBeginStageUnitReq.h"

#include "../Session/GameBeginStageUnitSession.h"



AGameBeginStageTimingSystem::AGameBeginStageTimingSystem()
{
	PrimaryActorTick.bCanEverTick = true;
}

void AGameBeginStageTimingSystem::Tick(float DeltaSeconds)
{
	OnTickUpdateRemainingTime(DeltaSeconds);
	OnTickDebugRemainingTime();
}

FString AGameBeginStageTimingSystem::GetHandlePath() const
{
	return GameBeginStageUnitReq::GameBeginStageStartCountDown::Path();
}

void AGameBeginStageTimingSystem::HandleRequest(FRequestPtr InOutRequest, FResponsePtr InOutResponse)
{
	GEngine->AddOnScreenDebugMessage(-1, 5, FColor::Red, "AGameBeginStageTimingSystem", false);

	StartTiming(6);
}

void AGameBeginStageTimingSystem::RegisterUnitSession()
{
	SetUnitSession(AGameBeginStageUnitSession::StaticClass());
}

void AGameBeginStageTimingSystem::RegisterEntityComps()
{
}

void AGameBeginStageTimingSystem::RegisterRequests()
{
	RegisterRequest(GlobalRequestPath::ChangeGameStage::Path());
}

void AGameBeginStageTimingSystem::OnTickUpdateRemainingTime(float DeltaSeconds)
{
	AGameBeginStageUnitSession* session = GetUnitSession<AGameBeginStageUnitSession>();
	if (session->GetIsTiming() == true)
	{
		RemainingTime -= DeltaSeconds;
		if (RemainingTime < 0)
		{
			OnTimingEnd();
		}
	}
}

void AGameBeginStageTimingSystem::OnTimingEnd()
{
	AGameBeginStageUnitSession* session = GetUnitSession<AGameBeginStageUnitSession>();

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

void AGameBeginStageTimingSystem::OnTickDebugRemainingTime()
{
	// Songlingyi Debug
	AGameBeginStageUnitSession* session = GetUnitSession<AGameBeginStageUnitSession>();
	if (session->GetIsTiming() == true)
	{
		FString str = "GameBeginStage RemainingTime : " + FString::SanitizeFloat(RemainingTime);
		GEngine->AddOnScreenDebugMessage(-1, 0, FColor::Green, str, false);
	}
}

void AGameBeginStageTimingSystem::StartTiming(float InRemainingTime)
{
	// 1. set is timing in session
	AGameBeginStageUnitSession* session = GetUnitSession<AGameBeginStageUnitSession>();
	session->SetIsTiming(true);

	// 2. set RemainingTime
	RemainingTime = InRemainingTime;
}


// Fill out your copyright notice in the Description page of Project Settings.

#include "StageCore.h"
#include "EnterWaitForPlayerStageSystem.h"
#include "DeviceActionMessage.h"
#include "TSMHand.h"
#include "TSMWorldConfig.h"
#include "DeviceControlState.h"
#include "GlobalRequestPath.h"

#include "../Utils/WaitForPlayerStageUnitReq.h"

#include "../Session/WaitForPlayerStageUnitSession.h"

#include "Message.h"
#include "SystemMessagePath.h"
#include "TSMApp.h"

FString AEnterWaitForPlayerStageSystem::GetHandlePath() const
{
	return WaitForPlayerStageUnitReq::EnterWaitForPlayerStage::Path();
}

void AEnterWaitForPlayerStageSystem::HandleRequest(FRequestPtr InOutRequest, FResponsePtr InOutResponse)
{
	GEngine->AddOnScreenDebugMessage(-1, 5, FColor::Purple, "AEnterWaitForPlayerStageSystem", false);

	FRequestPtr req = FRequest::CreateRequest(
		WaitForPlayerStageUnitReq::WaitForPlayerStageStartCountDown::Path());
	SendRequest(req);
}

void AEnterWaitForPlayerStageSystem::RegisterUnitSession()
{
	SetUnitSession(AWaitForPlayerStageUnitSession::StaticClass());
}

void AEnterWaitForPlayerStageSystem::RegisterEntityComps()
{
}

void AEnterWaitForPlayerStageSystem::RegisterRequests()
{
	RegisterRequest(WaitForPlayerStageUnitReq::WaitForPlayerStageStartCountDown::Path());
}

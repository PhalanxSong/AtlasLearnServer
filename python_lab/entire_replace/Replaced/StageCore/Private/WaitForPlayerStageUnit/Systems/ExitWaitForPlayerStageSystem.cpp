// Fill out your copyright notice in the Description page of Project Settings.

#include "StageCore.h"
#include "ExitWaitForPlayerStageSystem.h"
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

FString AExitWaitForPlayerStageSystem::GetHandlePath() const
{
	return WaitForPlayerStageUnitReq::ExitWaitForPlayerStage::Path();
}

void AExitWaitForPlayerStageSystem::HandleRequest(FRequestPtr InOutRequest, FResponsePtr InOutResponse)
{
	GEngine->AddOnScreenDebugMessage(-1, 5, FColor::Purple, "AExitWaitForPlayerStageSystem", false);

	AWaitForPlayerStageUnitSession* session = GetUnitSession<AWaitForPlayerStageUnitSession>();
	session->SetIsTiming(false);
}

void AExitWaitForPlayerStageSystem::RegisterUnitSession()
{
	SetUnitSession(AWaitForPlayerStageUnitSession::StaticClass());
}

void AExitWaitForPlayerStageSystem::RegisterEntityComps()
{
}

void AExitWaitForPlayerStageSystem::RegisterRequests()
{
	//RegisterRequest(GlobalRequestPath::ChangeGameStage::Path());
}

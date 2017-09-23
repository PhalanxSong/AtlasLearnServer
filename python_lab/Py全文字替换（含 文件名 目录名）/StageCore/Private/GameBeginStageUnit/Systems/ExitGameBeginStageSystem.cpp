// Fill out your copyright notice in the Description page of Project Settings.

#include "StageCore.h"
#include "ExitGameBeginStageSystem.h"
#include "DeviceActionMessage.h"
#include "TSMHand.h"
#include "TSMWorldConfig.h"
#include "DeviceControlState.h"
#include "GlobalRequestPath.h"

#include "../Utils/GameBeginStageUnitReq.h"

#include "../Session/GameBeginStageUnitSession.h"

#include "Message.h"
#include "SystemMessagePath.h"
#include "TSMApp.h"

FString AExitGameBeginStageSystem::GetHandlePath() const
{
	return GameBeginStageUnitReq::ExitGameBeginStage::Path();
}

void AExitGameBeginStageSystem::HandleRequest(FRequestPtr InOutRequest, FResponsePtr InOutResponse)
{
	GEngine->AddOnScreenDebugMessage(-1, 5, FColor::Purple, "AExitGameBeginStageSystem", false);
}

void AExitGameBeginStageSystem::RegisterUnitSession()
{
	SetUnitSession(AGameBeginStageUnitSession::StaticClass());
}

void AExitGameBeginStageSystem::RegisterEntityComps()
{
}

void AExitGameBeginStageSystem::RegisterRequests()
{
	RegisterRequest(GlobalRequestPath::ChangeGameStage::Path());
}

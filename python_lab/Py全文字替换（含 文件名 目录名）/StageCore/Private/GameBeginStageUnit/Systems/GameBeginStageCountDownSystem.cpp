// Fill out your copyright notice in the Description page of Project Settings.

#include "StageCore.h"
#include "GameBeginStageCountDownSystem.h"
#include "DeviceActionMessage.h"
#include "TSMHand.h"
#include "TSMWorldConfig.h"
#include "DeviceControlState.h"
#include "GlobalRequestPath.h"

#include "Message.h"
#include "SystemMessagePath.h"
#include "TSMApp.h"

#include "../Utils/GameBeginStageUnitReq.h"

#include "../Session/GameBeginStageUnitSession.h"

FString AGameBeginStageCountDownSystem::GetHandlePath() const
{
	return GameBeginStageUnitReq::GameBeginStageStartCountDown::Path();
}

void AGameBeginStageCountDownSystem::HandleRequest(FRequestPtr InOutRequest, FResponsePtr InOutResponse)
{
	GEngine->AddOnScreenDebugMessage(-1, 5, FColor::Red, "AGameBeginStageCountDownSystem", false);
}

void AGameBeginStageCountDownSystem::RegisterUnitSession()
{
	SetUnitSession(AGameBeginStageUnitSession::StaticClass());
}

void AGameBeginStageCountDownSystem::RegisterEntityComps()
{
}

void AGameBeginStageCountDownSystem::RegisterRequests()
{
}

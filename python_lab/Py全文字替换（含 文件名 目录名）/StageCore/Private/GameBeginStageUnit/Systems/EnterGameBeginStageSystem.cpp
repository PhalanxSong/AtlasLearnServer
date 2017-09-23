// Fill out your copyright notice in the Description page of Project Settings.

#include "StageCore.h"
#include "EnterGameBeginStageSystem.h"
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

FString AEnterGameBeginStageSystem::GetHandlePath() const
{
	return GameBeginStageUnitReq::EnterGameBeginStage::Path();
}

void AEnterGameBeginStageSystem::HandleRequest(FRequestPtr InOutRequest, FResponsePtr InOutResponse)
{
	GEngine->AddOnScreenDebugMessage(-1, 5, FColor::Purple, "AEnterGameBeginStageSystem", false);
}

void AEnterGameBeginStageSystem::RegisterUnitSession()
{
	SetUnitSession(AGameBeginStageUnitSession::StaticClass());
}

void AEnterGameBeginStageSystem::RegisterEntityComps()
{
}

void AEnterGameBeginStageSystem::RegisterRequests()
{
}

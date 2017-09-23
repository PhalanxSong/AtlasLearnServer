// Fill out your copyright notice in the Description page of Project Settings.

#include "StageCore.h"
#include "WaitForPlayerStageUnitRegister.h"
#include "PawnStateRegistry.h"
#include "DeviceControlState.h"
#include "MessageRouter.h"
#include "SystemMessageAction.h"
#include "SystemMessagePath.h"
#include "DeviceMessagePath.h"
#include "UnitRegistry.h"
#include "UIControlMessagePath.h"
#include "DeviceMessageAction.h"
#include "GlobalRequestPath.h"

#include "Private/GameStageManager/GameStageManager.h"

#include "Utils/WaitForPlayerStageUnitReq.h"

#include "Session/WaitForPlayerStageUnitSession.h"

#include "Systems/EnterWaitForPlayerStageSystem.h"
#include "Systems/ExitWaitForPlayerStageSystem.h"
#include "Systems/WaitForPlayerStageTimingSystem.h"

WaitForPlayerStageUnitRegister::WaitForPlayerStageUnitRegister()
{
}

WaitForPlayerStageUnitRegister::~WaitForPlayerStageUnitRegister()
{
}

void WaitForPlayerStageUnitRegister::RegisterSystems()
{
	UnitRegistry::RegisterSystem(WaitForPlayerStageUnitName, AEnterWaitForPlayerStageSystem::StaticClass());
	UnitRegistry::RegisterSystem(WaitForPlayerStageUnitName, AExitWaitForPlayerStageSystem::StaticClass());
	UnitRegistry::RegisterSystem(WaitForPlayerStageUnitName, AWaitForPlayerStageTimingSystem::StaticClass());
}

void WaitForPlayerStageUnitRegister::RegisterUnitSession()
{
	UnitRegistry::RegisterSession(AWaitForPlayerStageUnitSession::StaticClass());
}

void WaitForPlayerStageUnitRegister::RegisterRouter()
{
	MessageRouter::Instance().RegisterSystemMessage(
		SystemMessagePath::GameStage::JoinOnAfterStageEnterPath(GameStageName::WaitForPlayerStage, true),
		WaitForPlayerStageUnitReq::EnterWaitForPlayerStage::Path()
		);

	MessageRouter::Instance().RegisterSystemMessage(
		SystemMessagePath::GameStage::JoinOnAfterStageEnterPath(GameStageName::WaitForPlayerStage, false),
		WaitForPlayerStageUnitReq::EnterWaitForPlayerStage::Path()
		);

	MessageRouter::Instance().RegisterSystemMessage(
		SystemMessagePath::GameStage::JoinOnBeforeStageExitPath(GameStageName::WaitForPlayerStage, true),
		WaitForPlayerStageUnitReq::ExitWaitForPlayerStage::Path()
		);

	MessageRouter::Instance().RegisterSystemMessage(
		SystemMessagePath::GameStage::JoinOnBeforeStageExitPath(GameStageName::WaitForPlayerStage, false),
		WaitForPlayerStageUnitReq::ExitWaitForPlayerStage::Path()
		);
}

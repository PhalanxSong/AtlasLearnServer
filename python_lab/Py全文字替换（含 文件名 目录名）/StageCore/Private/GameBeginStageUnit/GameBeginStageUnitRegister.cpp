// Fill out your copyright notice in the Description page of Project Settings.

#include "StageCore.h"
#include "GameBeginStageUnitRegister.h"
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

#include "Utils/GameBeginStageUnitReq.h"

#include "Session/GameBeginStageUnitSession.h"

#include "Systems/EnterGameBeginStageSystem.h"
#include "Systems/ExitGameBeginStageSystem.h"
#include "Systems/GameBeginStageCountDownSystem.h"

GameBeginStageUnitRegister::GameBeginStageUnitRegister()
{
}

GameBeginStageUnitRegister::~GameBeginStageUnitRegister()
{
}

void GameBeginStageUnitRegister::RegisterSystems()
{
	UnitRegistry::RegisterSystem(GameBeginStageUnitName, AEnterGameBeginStageSystem::StaticClass());
	UnitRegistry::RegisterSystem(GameBeginStageUnitName, AExitGameBeginStageSystem::StaticClass());
	UnitRegistry::RegisterSystem(GameBeginStageUnitName, AGameBeginStageCountDownSystem::StaticClass());
}

void GameBeginStageUnitRegister::RegisterUnitSession()
{
	UnitRegistry::RegisterSession(AGameBeginStageUnitSession::StaticClass());
}

void GameBeginStageUnitRegister::RegisterRouter()
{
	MessageRouter::Instance().RegisterSystemMessage(
		SystemMessagePath::GameStage::JoinOnAfterStageEnterPath(GameStageName::GameBeginStage),
		GameBeginStageUnitReq::EnterGameBeginStage::Path()
		);

	MessageRouter::Instance().RegisterSystemMessage(
		SystemMessagePath::GameStage::JoinOnBeforeStageExitPath(GameStageName::GameBeginStage),
		GameBeginStageUnitReq::ExitGameBeginStage::Path()
		);
}

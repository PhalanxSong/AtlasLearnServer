// Fill out your copyright notice in the Description page of Project Settings.

#pragma once
#include "UnitRegisterInterface.h"

class STAGECORE_API WaitForPlayerStageUnitRegister : public UnitRegisterInterface
{
public:
	WaitForPlayerStageUnitRegister();
	~WaitForPlayerStageUnitRegister();
	virtual void RegisterSystems() override;
	virtual void RegisterComponents() override {}
	virtual void RegisterEntities() override {}
	virtual void RegisterUnitSession() override;
	virtual void RegisterRouter() override;
};

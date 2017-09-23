// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "UnitTemplate/UnitSession.h"
#include "WaitForPlayerStageUnitSession.generated.h"

UCLASS()
class STAGECORE_API AWaitForPlayerStageUnitSession : public AUnitSession
{
	GENERATED_BODY()

public:

	void SetIsTiming(bool bInIsTiming);

	bool GetIsTiming();

private:

	bool bIsTiming = false;

};

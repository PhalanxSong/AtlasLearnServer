// Fill out your copyright notice in the Description page of Project Settings.

#include "StageCore.h"
#include "GameBeginStageUnitSession.h"

void AGameBeginStageUnitSession::SetIsTiming(bool bInIsTiming)
{
	bIsTiming = bInIsTiming;
}

bool AGameBeginStageUnitSession::GetIsTiming()
{
	return bIsTiming;
}

// Fill out your copyright notice in the Description page of Project Settings.

#include "StageCore.h"
#include "WaitForPlayerStageUnitSession.h"

void AWaitForPlayerStageUnitSession::SetIsTiming(bool bInIsTiming)
{
	bIsTiming = bInIsTiming;
}

bool AWaitForPlayerStageUnitSession::GetIsTiming()
{
	return bIsTiming;
}

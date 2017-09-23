// Fill out your copyright notice in the Description page of Project Settings.

#include "StageCore.h"
#include "WaitForPlayerStageUnitReq.h"
#include "MessageUtil.h"

const FString WaitForPlayerStageUnitReq::EnterWaitForPlayerStage::Path()
{
	FString str = "EnterWaitForPlayerStage";
	return str;
}

const FString WaitForPlayerStageUnitReq::ExitWaitForPlayerStage::Path()
{
	FString str = "ExitWaitForPlayerStage";
	return str;
}

const FString WaitForPlayerStageUnitReq::WaitForPlayerStageStartCountDown::Path()
{
	FString str = "WaitForPlayerStageStartCountDown";
	return str;
}

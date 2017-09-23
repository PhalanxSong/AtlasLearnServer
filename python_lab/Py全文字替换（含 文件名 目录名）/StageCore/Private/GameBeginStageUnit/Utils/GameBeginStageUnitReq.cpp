// Fill out your copyright notice in the Description page of Project Settings.

#include "StageCore.h"
#include "GameBeginStageUnitReq.h"
#include "MessageUtil.h"

const FString GameBeginStageUnitReq::EnterGameBeginStage::Path()
{
	FString str = "EnterGameBeginStage";
	return str;
}

const FString GameBeginStageUnitReq::ExitGameBeginStage::Path()
{
	FString str = "ExitGameBeginStage";
	return str;
}

const FString GameBeginStageUnitReq::GameBeginStageStartCountDown::Path()
{
	FString str = "GameBeginStageStartCountDown";
	return str;
}

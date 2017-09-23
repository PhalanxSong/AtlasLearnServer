// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

struct STAGECORE_API WaitForPlayerStageUnitReq
{
	struct STAGECORE_API EnterWaitForPlayerStage
	{
		static const FString Path();
	};

	struct STAGECORE_API ExitWaitForPlayerStage
	{
		static const FString Path();
	};

	struct STAGECORE_API WaitForPlayerStageStartCountDown
	{
		static const FString Path();
	};
};

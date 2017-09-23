// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

struct STAGECORE_API GameBeginStageUnitReq
{
	struct STAGECORE_API EnterGameBeginStage
	{
		static const FString Path();
	};

	struct STAGECORE_API ExitGameBeginStage
	{
		static const FString Path();
	};

	struct STAGECORE_API GameBeginStageStartCountDown
	{
		static const FString Path();
	};
};

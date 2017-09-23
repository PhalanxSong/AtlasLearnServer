// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "PrimitiveSystemUnit/RequestHandlerSystem.h"
#include "GameBeginStageTimingSystem.generated.h"

UCLASS()
class STAGECORE_API AGameBeginStageTimingSystem : public ARequestHandlerSystem
{
	GENERATED_BODY()

public:

	AGameBeginStageTimingSystem();

	virtual void Tick(float DeltaSeconds) override;

	virtual FString GetHandlePath() const override;

	virtual void HandleRequest(FRequestPtr InOutRequest, FResponsePtr InOutResponse) override;

	virtual void RegisterUnitSession() override;

	virtual void RegisterEntityComps() override;

	void RegisterRequests() override;

private:

	void OnTickUpdateRemainingTime(float DeltaSeconds);

	void OnTimingEnd();

	void OnTickDebugRemainingTime();

	void StartTiming(float InRemainingTime);

	float RemainingTime = 0;

};

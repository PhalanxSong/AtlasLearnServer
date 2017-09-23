// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "PrimitiveSystemUnit/RequestHandlerSystem.h"
#include "ExitWaitForPlayerStageSystem.generated.h"

UCLASS()
class STAGECORE_API AExitWaitForPlayerStageSystem : public ARequestHandlerSystem
{
	GENERATED_BODY()

public:

	virtual FString GetHandlePath() const override;

	virtual void HandleRequest(FRequestPtr InOutRequest, FResponsePtr InOutResponse) override;

	virtual void RegisterUnitSession() override;

	virtual void RegisterEntityComps() override;

	void RegisterRequests() override;

};

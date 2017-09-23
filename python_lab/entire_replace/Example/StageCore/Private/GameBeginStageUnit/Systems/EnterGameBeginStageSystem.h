// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "PrimitiveSystemUnit/RequestHandlerSystem.h"
#include "EnterGameBeginStageSystem.generated.h"

UCLASS()
class STAGECORE_API AEnterGameBeginStageSystem : public ARequestHandlerSystem
{
	GENERATED_BODY()

public:

	virtual FString GetHandlePath() const override;

	virtual void HandleRequest(FRequestPtr InOutRequest, FResponsePtr InOutResponse) override;

	virtual void RegisterUnitSession() override;

	virtual void RegisterEntityComps() override;

	void RegisterRequests() override;

};

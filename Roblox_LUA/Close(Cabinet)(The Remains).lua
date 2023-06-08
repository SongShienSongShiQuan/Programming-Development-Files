local function  Drawer_Control_1()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local targetA1 = sc

	local target_posA1 = sc.Parent.Position2_D2
	local target_posA2 = sc.Parent.Position1_D2

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(targetA1, tweenInfo, {Position = target_posA1.Position})

	local tweensecond = TweenService:Create(targetA1, tweenInfo, {Position = target_posA2.Position})


	tweenfirst:Play()
end

local function  Drawer_Control_2()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local targetA1 = sc

	local target_posA1 = sc.Parent.Position2_D2
	local target_posA2 = sc.Parent.Position1_D2

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(targetA1, tweenInfo, {Position = target_posA1.Position})

	local tweensecond = TweenService:Create(targetA1, tweenInfo, {Position = target_posA2.Position})


	tweensecond:Play()
end
Drawer_Control_2()
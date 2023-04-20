local Pool = true
local directselect = game.Workspace["MRT0-27 A2"]

local directselectB = game.Workspace["MRT0-27 A2"].AnchorPartsParent

local selectionA = game.Workspace["MRT0-27 A2"].A
local lock = false

local function  Door_Control_R1_ANIM1()
	
	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

			local target = sc.Target
	local targetF = sc.TargetA
	
	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].Control["DOOR B - R"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end
	
	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].Control["DOOR B - R"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end
	

	
				local targetB = sc["B-Target"]
				local targetBA = sc["B-TargetA"]

				local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

			local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})
	
	local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()
	
	tweensecond:Play()
	wait(1)
	SELECT()
	SELECT2()

end



local function  Door_Control_R1_ANIM2()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

								local target = sc.Target
	local targetF = sc.TargetA
	
	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].Control["DOOR B - R"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end

	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].Control["DOOR B - R"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end




									local targetB = sc["A-Target"]
										local targetBA = sc["A-TargetA"]

										local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

										local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})

								local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()

	tweensecond:Play()
	
	wait(1)
	SELECT()
	SELECT2()
end






local function  Door_Control_R2_ANIM1()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local target = game.Workspace["MRT0-27 A2"].Control["DOOR A - R"].Target
	local targetF = game.Workspace["MRT0-27 A2"].Control["DOOR A - R"].TargetA

	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].Control["DOOR A - R"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end

	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].Control["DOOR A - R"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end



	local targetB = game.Workspace["MRT0-27 A2"].Control["DOOR A - R"]["B-Target"]
	local targetBA = game.Workspace["MRT0-27 A2"].Control["DOOR A - R"]["B-TargetA"]

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})

	local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()

	tweensecond:Play()
	wait(1)
	SELECT()
	SELECT2()
end



local function  Door_Control_R2_ANIM2()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local target = game.Workspace["MRT0-27 A2"].Control["DOOR A - R"].Target
	local targetF = game.Workspace["MRT0-27 A2"].Control["DOOR A - R"].TargetA

	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].Control["DOOR A - R"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end

	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].Control["DOOR A - R"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end





	local targetB = game.Workspace["MRT0-27 A2"].Control["DOOR A - R"]["A-Target"]
	local targetBA = game.Workspace["MRT0-27 A2"].Control["DOOR A - R"]["A-TargetA"]

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})

	local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()

	tweensecond:Play()
	
	wait(1)
	SELECT()
	SELECT2()

end












local function  Door_A_R1_ANIM1()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local target = game.Workspace["MRT0-27 A2"].A["DOOR A - R"].Target
	local targetF = game.Workspace["MRT0-27 A2"].A["DOOR A - R"].TargetA

	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].A["DOOR A - R"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end

	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].A["DOOR A - R"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end



	local targetB = game.Workspace["MRT0-27 A2"].A["DOOR A - R"]["B-Target"]
	local targetBA = game.Workspace["MRT0-27 A2"].A["DOOR A - R"]["B-TargetA"]

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})

	local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()

	tweensecond:Play()
	
	wait(1)
	SELECT()
	SELECT2()
end



local function  Door_A_R1_ANIM2()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local target = game.Workspace["MRT0-27 A2"].A["DOOR A - R"].Target
	local targetF = game.Workspace["MRT0-27 A2"].A["DOOR A - R"].TargetA

	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].A["DOOR A - R"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end

	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].A["DOOR A - R"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end





	local targetB = game.Workspace["MRT0-27 A2"].A["DOOR A - R"]["A-Target"]
	local targetBA = game.Workspace["MRT0-27 A2"].A["DOOR A - R"]["A-TargetA"]

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})

	local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()

	tweensecond:Play()
	
	wait(1)
	SELECT()
	SELECT2()

end














local function  Door_ControlB_R1_ANIM1()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local target = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR B - R"].Target
	local targetF = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR B - R"].TargetA

	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"]["Control B"]["DOOR B - R"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end

	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"]["Control B"]["DOOR B - R"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end



	local targetB = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR B - R"]["B-Target"]
	local targetBA = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR B - R"]["B-TargetA"]

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})

	local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()

	tweensecond:Play()

	wait(1)
	SELECT()
	SELECT2()
end



local function  Door_ControlB_R1_ANIM2()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local target = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR B - R"].Target
	local targetF = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR B - R"].TargetA

	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"]["Control B"]["DOOR B - R"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end

	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"]["Control B"]["DOOR B - R"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end





	local targetB = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR B - R"]["A-Target"]
	local targetBA = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR B - R"]["A-TargetA"]

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})

	local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()

	tweensecond:Play()

	wait(1)
	SELECT()
	SELECT2()

end












local function  Door_ControlB_R2_ANIM1()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local target = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR A - R"].Target
	local targetF = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR A - R"].TargetA

	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"]["Control B"]["DOOR A - R"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end

	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"]["Control B"]["DOOR A - R"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end



	local targetB = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR A - R"]["B-Target"]
	local targetBA = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR A - R"]["B-TargetA"]

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})

	local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()

	tweensecond:Play()

	wait(1)
	SELECT()
	SELECT2()
end



local function  Door_ControlB_R2_ANIM2()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local target = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR A - R"].Target
	local targetF = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR A - R"].TargetA

	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"]["Control B"]["DOOR A - R"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end

	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"]["Control B"]["DOOR A - R"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end





	local targetB = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR A - R"]["A-Target"]
	local targetBA = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR A - R"]["A-TargetA"]

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})

	local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()

	tweensecond:Play()

	wait(1)
	SELECT()
	SELECT2()

end


local function  Door_Control_L1_ANIM1()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local target = sc.Parent["DOOR C - L"].Target
	local targetF = sc.Parent["DOOR C - L"].TargetA

	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].Control["DOOR C - L"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end

	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].Control["DOOR C - L"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end



	local targetB = sc.Parent["DOOR C - L"]["B-Target"]
	local targetBA = sc.Parent["DOOR C - L"]["B-TargetA"]

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})

	local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()

	tweensecond:Play()
	wait(1)
	SELECT()
	SELECT2()

end


local function  Door_Control_L1_ANIM2()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local target = sc.Parent["DOOR C - L"].Target
	local targetF = sc.Parent["DOOR C - L"].TargetA

	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].Control["DOOR C - L"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end

	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].Control["DOOR C - L"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end




	local targetB = sc.Parent["DOOR C - L"]["A-Target"]
	local targetBA = sc.Parent["DOOR C - L"]["A-TargetA"]

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})

	local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()

	tweensecond:Play()

	wait(1)
	SELECT()
	SELECT2()
end

local function  Door_Control_L2_ANIM1()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local target = sc.Parent["DOOR D - L"].Target
	local targetF = sc.Parent["DOOR D - L"].TargetA

	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].Control["DOOR D - L"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end

	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].Control["DOOR D - L"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end



	local targetB = sc.Parent["DOOR D - L"]["B-Target"]
	local targetBA = sc.Parent["DOOR D - L"]["B-TargetA"]

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})

	local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()

	tweensecond:Play()
	wait(1)
	SELECT()
	SELECT2()

end

local function  Door_Control_L2_ANIM2()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local target = sc.Parent["DOOR D - L"].Target
	local targetF = sc.Parent["DOOR D - L"].TargetA

	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].Control["DOOR D - L"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end

	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].Control["DOOR D - L"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end




	local targetB = sc.Parent["DOOR D - L"]["A-Target"]
	local targetBA = sc.Parent["DOOR D - L"]["A-TargetA"]

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})

	local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()

	tweensecond:Play()

	wait(1)
	SELECT()
	SELECT2()
end









local function  Door_A_L1_ANIM1()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local target = game.Workspace["MRT0-27 A2"].A["DOOR B - L"].Target
	local targetF = game.Workspace["MRT0-27 A2"].A["DOOR B - L"].TargetA

	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].A["DOOR B - L"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end

	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].A["DOOR B - L"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end



	local targetB = game.Workspace["MRT0-27 A2"].A["DOOR B - L"]["B-Target"]
	local targetBA = game.Workspace["MRT0-27 A2"].A["DOOR B - L"]["B-TargetA"]

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})

	local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()

	tweensecond:Play()

	wait(1)
	SELECT()
	SELECT2()
end



local function  Door_A_L1_ANIM2()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local target = game.Workspace["MRT0-27 A2"].A["DOOR B - L"].Target
	local targetF = game.Workspace["MRT0-27 A2"].A["DOOR B - L"].TargetA

	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].A["DOOR B - L"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end

	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"].A["DOOR B - L"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end





	local targetB = game.Workspace["MRT0-27 A2"].A["DOOR B - L"]["A-Target"]
	local targetBA = game.Workspace["MRT0-27 A2"].A["DOOR B - L"]["A-TargetA"]

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})

	local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()

	tweensecond:Play()

	wait(1)
	SELECT()
	SELECT2()

end




local function  Door_ControlB_L1_ANIM1()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local target = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR C - L"].Target
	local targetF = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR C - L"].TargetA

	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"]["Control B"]["DOOR C - L"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end

	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"]["Control B"]["DOOR C - L"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end



	local targetB = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR C - L"]["B-Target"]
	local targetBA = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR C - L"]["B-TargetA"]

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})

	local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()

	tweensecond:Play()

	wait(1)
	SELECT()
	SELECT2()
end



local function  Door_ControlB_L1_ANIM2()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local target = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR C - L"].Target
	local targetF = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR C - L"].TargetA

	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"]["Control B"]["DOOR C - L"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end

	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"]["Control B"]["DOOR C - L"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end





	local targetB = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR C - L"]["A-Target"]
	local targetBA = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR C - L"]["A-TargetA"]

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})

	local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()

	tweensecond:Play()

	wait(1)
	SELECT()
	SELECT2()

end












local function  Door_ControlB_L2_ANIM1()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local target = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR D - L"].Target
	local targetF = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR D - L"].TargetA

	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"]["Control B"]["DOOR D - L"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end

	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"]["Control B"]["DOOR D - L"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 1
			end
		end
	end



	local targetB = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR D - L"]["B-Target"]
	local targetBA = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR D - L"]["B-TargetA"]

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})

	local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()

	tweensecond:Play()

	wait(1)
	SELECT()
	SELECT2()
end



local function  Door_ControlB_L2_ANIM2()

	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local target = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR D - L"].Target
	local targetF = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR D - L"].TargetA

	local function SELECT()
		for _, i in pairs(game.Workspace["MRT0-27 A2"]["Control B"]["DOOR D - L"].Target:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end

	local function SELECT2()
		for _, i in pairs(game.Workspace["MRT0-27 A2"]["Control B"]["DOOR D - L"].TargetA:GetChildren()) do
			if i:IsA("MeshPart") then
				i.Transparency = 0
			end
		end
	end





	local targetB = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR D - L"]["A-Target"]
	local targetBA = game.Workspace["MRT0-27 A2"]["Control B"]["DOOR D - L"]["A-TargetA"]

	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)			

	local tweenfirst = TweenService:Create(target, tweenInfo, {Position = targetB.Position})

	local tweensecond = TweenService:Create(targetF, tweenInfo, {Position = targetBA.Position})


	tweenfirst:Play()

	tweensecond:Play()

	wait(1)
	SELECT()
	SELECT2()

end


















local function  Move()
	local TweenService = game:GetService("TweenService")
				local sc = script.Parent
	
				local maintarget = game.Workspace.FIRSTSTATIONA
	
	maintarget.CFrame = CFrame.new(maintarget.Position) + Vector3.new(0, 5, 0)
end

			local function  MoveNext()
						local TweenService = game:GetService("TweenService")
							local sc = script.Parent

								local maintarget = game.Workspace.FIRSTSTATIONA

			maintarget.CFrame = CFrame.new(maintarget.Position) + Vector3.new(0, -5, 0)
end


local function  MoveB()
	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local maintarget = game.Workspace.FIRSTSTATIONBA

	maintarget.CFrame = CFrame.new(maintarget.Position) + Vector3.new(0, 5, 0)
end

local function  MoveNextB()
	local TweenService = game:GetService("TweenService")
	local sc = script.Parent

	local maintarget = game.Workspace.FIRSTSTATIONBA

	maintarget.CFrame = CFrame.new(maintarget.Position) + Vector3.new(0, -5, 0)
end





local function ACTUALLOCK() --Local Functions call if needed this type of function.
	for _, i in pairs(directselect:GetDescendants()) do
		if i:IsA("Part") then

					lock = true print("LINE SUCCESS")

			i.Anchored = true
		end
	end
end



local function REMOVELOCK() --Local Functions call if needed this type of function.
	for _, i in pairs(directselect:GetDescendants()) do
		if i:IsA("Part") then

					lock = true print("LINE SUCCESS")

					i.Anchored = false
		end
	end
end


local function TRAINSOUNDCOLLECTION() --Local Functions call if needed this type of function.
	for _, i in pairs(directselectB:GetDescendants()) do
		if i:IsA("Sound") then
			i:Play()
		end
	end
end

local function MotorsSound() --Local Functions call if needed this type of function.
	for _, i in pairs(selectionA:GetDescendants()) do
		if i:IsA("Sound") then
			i:Play()
			i.Volume = 0.5
			i.TimePosition = 0
		end
	end
end

local function MotorsSoundStop() --Local Functions call if needed this type of function.
	for _, i in pairs(selectionA:GetDescendants()) do
		if i:IsA("Sound") then
			i.Volume = 0.1
		end
	end
end



local function Reset()
	local directselectmain = game.Workspace["MRT0-27 A2"]
	directselect.Configuration.Disabled = true
	wait(1)
	directselect.Configuration.Disabled = false
end





local function LightChangeA()
	local directselect = game.Workspace["MRT0-27 A2"]
	directselect.Control.LampuA.Red.Enabled = false
	directselect.Control.LampuA.White.Enabled = true
	directselect.Control.LampuACB.Transparency = 1
	directselect["Control B"].LampuACB.Transparency = 0
	directselect.Control.LampuAC.Transparency = 0
	directselect["Control B"].LampuAC.Transparency = 1
	directselect["Control B"].LampuA.Red.Enabled = true
	directselect["Control B"].LampuA.White.Enabled = false
end

local function LightChangeB()
	local directselect = game.Workspace["MRT0-27 A2"]
	directselect.Control.LampuA.Red.Enabled = true
	directselect.Control.LampuA.White.Enabled = false
	directselect.Control.LampuACB.Transparency = 0
	directselect["Control B"].LampuACB.Transparency = 1
	directselect.Control.LampuAC.Transparency = 1
	directselect["Control B"].LampuAC.Transparency = 0
	directselect["Control B"].LampuA.Red.Enabled = false
	directselect["Control B"].LampuA.White.Enabled = true
end



local gm = game.Workspace
local maintarget = game.Workspace.FIRSTSTATIONA

local actualtarget = game.Workspace["MRT0-27 A2"]

local lock = false

maintarget.Touched:Connect(function(TouchPartIs)
	if not lock then
	lock = true
	
	ACTUALLOCK()
	Move()
		MotorsSoundStop()
		LightChangeB()

	
	print("Working")
	wait(1)
			TRAINSOUNDCOLLECTION()
		  	Door_Control_L1_ANIM1()
			Door_Control_L2_ANIM1()
			Door_A_L1_ANIM1()	
			Door_ControlB_L1_ANIM1()
			Door_ControlB_L2_ANIM1()
	wait(5)
			TRAINSOUNDCOLLECTION()
			Door_Control_L1_ANIM2()
			Door_Control_L2_ANIM2()
			Door_A_L1_ANIM2()
			Door_ControlB_L1_ANIM2()
			Door_ControlB_L2_ANIM2()
	wait(5)	REMOVELOCK() MotorsSound() wait(30) MotorsSoundStop() MoveNext()
	lock = false
		
	end
	end)



local gm = game.Workspace
local maintargetB = game.Workspace.FIRSTSTATIONBA

local actualtarget = game.Workspace["MRT0-27 A2"]

local lock = false

maintargetB.Touched:Connect(function(TouchPartIs)
	if not lock then
	lock = true
	
	ACTUALLOCK()
		MoveB()
		MotorsSoundStop()
		LightChangeA()
		Reset()

	
		print("Working")
			wait(1)
				TRAINSOUNDCOLLECTION()
				Door_Control_R1_ANIM1()
				Door_Control_R2_ANIM1()
				Door_A_R1_ANIM1()
				Door_ControlB_R1_ANIM1()
				Door_ControlB_R2_ANIM1()
			wait(5)
				TRAINSOUNDCOLLECTION()
				Door_Control_R1_ANIM2()
				Door_Control_R2_ANIM2()
				Door_A_R1_ANIM2()
				Door_ControlB_R1_ANIM2()
				Door_ControlB_R2_ANIM2()
			wait(5)	REMOVELOCK() MotorsSound() wait(30) MotorsSoundStop() MoveNextB()
		lock = false
		
	end
	end)

--Formula Tween for "Parts, MeshPart, or Unions/CSG"

--local sc = script.Parent
--local Pool = true

--local function  TweenFirst()
--	local TweenService = game:GetService("TweenService")

--	local part = sc["Meshes/MRT 3 38"]

--	local tweenInfo = TweenInfo.new( 2, Enum.EasingStyle.Linear, Enum.EasingDirection.Out,-1, true, 0 )

--	local tween = TweenService:Create(sc["Meshes/MRT 3 38"], tweenInfo, {Position = Vector3.new(0, 30, 0)})

--	tween:Play()
--

--while Pool == true do
--	wait(5)
--	TweenFirst()
--end




--if TouchPartIs.Parent.Name == "TouchPart" then





--local function TRAINSOUNDCOLLECTION() --Local Functions call if needed this type of function.
--for _, i in pairs(directselect:GetDescendants()) do
			--if i.Name == PlayersHouse then
		---if i:IsA("Sound") then
		--	i:Play()
	--	end
--	end
--end
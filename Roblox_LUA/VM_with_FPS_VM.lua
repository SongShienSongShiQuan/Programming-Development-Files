local runService = game:GetService("RunService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local lock = false
local Main = script.Parent 
local character = script.Parent
local Character_VM = ReplicatedStorage.R15:Clone()
local VM_Root_Part = Instance.new("Part")
local VM_Root_Part_Weld = Instance.new("Weld")
local player = game.Players.LocalPlayer
local mouse = player:GetMouse()


local plr = player
local character_part = plr.Character
local mouse = plr:GetMouse()

local RightarmOffset = character_part.UpperTorso.CFrame:Inverse() * character_part.RightUpperArm.CFrame

local RightarmWeld = Instance.new("Weld")
RightarmWeld.Part0 = character_part.UpperTorso
RightarmWeld.Part1 = character_part.RightUpperArm
RightarmWeld.Parent = character_part
RightarmWeld.Name = "RightarmWeld"

local LeftarmOffset = character_part.UpperTorso.CFrame:Inverse() * character_part.LeftUpperArm.CFrame

local LeftarmWeld = Instance.new("Weld")
LeftarmWeld.Part0 = character_part.UpperTorso
LeftarmWeld.Part1 = character_part.LeftUpperArm
LeftarmWeld.Parent = character_part
LeftarmWeld.Name = "LeftarmWeld"


--VM_Root_Part.Name = "VM_Root_Part"
--VM_Root_Part.Parent = game.Workspace
--VM_Root_Part.CanCollide = false


runService.RenderStepped:Connect(function()
	--VM_Root_Part.CFrame = workspace.CurrentCamera.CFrame * CFrame.new(0,0,-10)
	local dist = (workspace.CurrentCamera.CFrame.Position - character.Head.Position).Magnitude

	local cframe = CFrame.new(character_part.UpperTorso.Position, mouse.Hit.Position) * CFrame.Angles(math.pi/5, 0, -6.5)
	RightarmWeld.C0 = RightarmOffset * character_part.UpperTorso.CFrame:toObjectSpace(cframe)

	local cframe = CFrame.new(character_part.UpperTorso.Position, mouse.Hit.Position) * CFrame.Angles(math.pi/5, 0, 6.5)
	LeftarmWeld.C0 = LeftarmOffset * character_part.UpperTorso.CFrame:toObjectSpace(cframe)

	if dist < 1 then
		character:FindFirstChild("RightUpperArm").LocalTransparencyModifier = 0
		character:FindFirstChild("LeftUpperArm").LocalTransparencyModifier = 0
		character:FindFirstChild("LeftLowerArm").LocalTransparencyModifier = 0
		character:FindFirstChild("LeftHand").LocalTransparencyModifier = 0
		character:FindFirstChild("RightLowerArm").LocalTransparencyModifier = 0
		character:FindFirstChild("RightHand").LocalTransparencyModifier = 0
	elseif dist > 1 then
		character:FindFirstChild("RightUpperArm").LocalTransparencyModifier = 0
		character:FindFirstChild("LeftUpperArm").LocalTransparencyModifier = 0
		character:FindFirstChild("LeftLowerArm").LocalTransparencyModifier = 0
		character:FindFirstChild("LeftHand").LocalTransparencyModifier = 0
		character:FindFirstChild("RightLowerArm").LocalTransparencyModifier = 0
		character:FindFirstChild("RightHand").LocalTransparencyModifier = 0
	end
end)

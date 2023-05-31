local runService = game:GetService("RunService")
local character = script.Parent
local mouse_follow = Instance.new("Part")
local weld = Instance.new("Weld")
local player = game.Players.LocalPlayer
local mouse = player:GetMouse()
local ReplicatedStorage = game:GetService("ReplicatedStorage")


runService.RenderStepped:Connect(function()
	local Camera = game.Workspace.CurrentCamera
	local player = game.Players.LocalPlayer
	local mouse = player:GetMouse()
	Camera.CameraType = Enum.CameraType.Scriptable

	mouse_follow.Name = "ROOT_HUMANOID"
	mouse_follow.Massless = true
	mouse_follow.CanCollide = false
	mouse_follow.Parent = character:FindFirstChild("UpperTorso")
	weld.Parent = mouse_follow
	weld.Part0 = mouse_follow
	weld.Part1 = character:FindFirstChild("UpperTorso")
	mouse_follow.CFrame = CFrame.lookAt(mouse_follow.Position, mouse.UnitRay.Direction)
end)

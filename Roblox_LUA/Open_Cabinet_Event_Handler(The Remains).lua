local ReplicatedStorage = game:GetService("ReplicatedStorage")

local RemoteEvent = ReplicatedStorage:WaitForChild("Open_Cabinet")

local function Handle_Event_Function(player, target)
	target.Open.Enabled = true
	wait(1)
	target.Open.Enabled = false
end

RemoteEvent.OnServerEvent:Connect(Handle_Event_Function)
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local RemoteEvent = ReplicatedStorage:WaitForChild("Close_Cabinet")

local function Handle_Event_Function(player, target)
	target.Close.Enabled = true
	wait(1)
	target.Close.Enabled = false
end

RemoteEvent.OnServerEvent:Connect(Handle_Event_Function)
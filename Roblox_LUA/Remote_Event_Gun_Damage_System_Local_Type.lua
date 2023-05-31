local ReplicatedStorage = game:GetService("ReplicatedStorage")
local ServerScriptService = game:GetService("ServerScriptService")
local remoteEvent = ReplicatedStorage:WaitForChild("Gun_Damage")
local function onCreatePart(player, human, partpos)
	print(player.Name .. " fired the RemoteEvent")
	local newPart = Instance.new("Part")
	newPart.Position = partpos
	human.Health = 0
end

remoteEvent.OnServerEvent:Connect(onCreatePart)
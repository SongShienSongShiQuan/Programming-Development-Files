local ReplicatedStorage = game:GetService("ReplicatedStorage")

local RemoteEvent = ReplicatedStorage:WaitForChild("DropItem")
local Items_Clone_RS = ReplicatedStorage.Items_Clone

local function Handle_Item_Stats(player, Item_Stats)
	Item_Stats.Value = Item_Stats.Value - 1
		local Item_Clone = Items_Clone_RS:FindFirstChild(Item_Stats.Name):Clone()
		if Item_Stats.Value >= 0 then
		Item_Clone.CFrame = player.Character.HumanoidRootPart.CFrame + player.Character.HumanoidRootPart.CFrame.LookVector * 3
		Item_Clone.Parent = game.Workspace
	end
end

RemoteEvent.OnServerEvent:Connect(Handle_Item_Stats)
local ServerStorage = game:GetService("ServerStorage")

local InventoryTemplate = ServerStorage:WaitForChild("InventoryTemplate")


game.Players.PlayerAdded:Connect(function(player)
	
	local GameData = InventoryTemplate:Clone()
	GameData.Name = "Item_Inventory"
	GameData.Parent = player
end)
local ServerStorage = game:GetService("ServerStorage")

local InventoryTemplate = ServerStorage:WaitForChild("InventoryTemplate")


local function SetupInventory(player)
	local Inventory = player:WaitForChild("Inventory")
	local PlayerGui = player:WaitForChild("PlayerGui")
	local MainGui = PlayerGui:WaitForChild("MainGui")
	local InventoryGui = MainGui:WaitForChild("InventoryGui")
	
	for i, item in pairs(Inventory:GetChildren())	do
		local itemGui = InventoryGui.Templates.Item:Clone()
		itemGui.Name = item.Name
		itemGui.ItemName.Text = item.Name
		itemGui.ItemQuantity.Text = item.Value
			if item.Value > 0 then
				itemGui.Visible = true
				itemGui.Parent = InventoryGui.ItemList
			else
				itemGui.Visible = false
				itemGui.Parent = InventoryGui.ItemList
			end
		end
	
end


game.Players.PlayerAdded:Connect(function(player)
	
	local GameData = InventoryTemplate:Clone()
	GameData.Name = "Inventory"
	GameData.Parent = player
	SetupInventory(player)
end)
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local TweenService = game:GetService("TweenService")

local Pickup_Event = ReplicatedStorage:WaitForChild("PickupItem")

local pickupTweenInfo = TweenInfo.new(
	.3,
	Enum.EasingStyle.Linear,
	Enum.EasingDirection.In,
	0,
	false,
	0
	)

local maxPickupDistance = 10

Pickup_Event.OnServerEvent:Connect(function(player, item)
	local char = player.Character
	local Item_Inventory = player.Item_Inventory
	
	local itemValue = Item_Inventory:FindFirstChild(item.Name)
	if itemValue then
		itemValue.Value = itemValue.Value + 1
		local finishingLocation = char.HumanoidRootPart.CFrame
		--for _, i in pairs(player.PlayerGui.Inventory_GUI.ScrollingFrame:GetDescendants()) do
			--if i.Name == item.Name then
				--i.Parent.Parent.Item_Count.Text = i.Parent.Parent.Item_Count.Text + 1
		item.CanCollide = false
		item.Anchored = true
		local tween = TweenService:Create(item, pickupTweenInfo, {Transparency = 1, Size = Vector3.new(0,0,0), CFrame = finishingLocation})
		tween:Play()
		tween.Completed:Connect(function()
		item:Destroy()
		end)
		end
		--end
	--end
end)
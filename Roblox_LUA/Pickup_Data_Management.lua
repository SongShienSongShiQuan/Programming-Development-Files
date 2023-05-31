local UIS = game:GetService("UserInputService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local PickupItem = ReplicatedStorage:WaitForChild("PickupItem")
local pickupKey = "E"

local player = game.Players.LocalPlayer
local mouse = player:GetMouse()

local PlayerGui = player:WaitForChild("PlayerGui")
local PickupInfoGui = PlayerGui:WaitForChild("PickupInfoGui")

UIS.InputChanged:Connect(function(input)
	if mouse.Target then
		if mouse.Target:FindFirstChild("Pickable") then
			local item = mouse.Target
			PickupInfoGui.Adornee = item
			PickupInfoGui.ObjectName.Text = item.Name
			PickupInfoGui.Enabled = true
		else
			PickupInfoGui.Adornee = nil
			PickupInfoGui.Enabled = false
		end
	end
end)


UIS.InputEnded:Connect(function(input)
	if input.KeyCode == Enum.KeyCode[pickupKey] then
		if mouse.Target then
			if mouse.Target:FindFirstChild("Pickable") then
				local item = mouse.Target
				if item then
					local distanceFromItem = player:DistanceFromCharacter(item.Position)
					if distanceFromItem < 30 then
						PickupItem:FireServer(item)
					end
				end
			end
		end
	end
end)
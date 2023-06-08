local UIS = game:GetService("UserInputService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Pickup_Event = ReplicatedStorage:WaitForChild("PickupItem")
local pickupKey = "E"

local player = game.Players.LocalPlayer
local mouse = player:GetMouse()

local PlayerGui = player:WaitForChild("PlayerGui")
local PickupInfoGui = PlayerGui:WaitForChild("Pickup_GUI")

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

local duplicate_preventer = true
UIS.InputEnded:Connect(function(input)
	if input.KeyCode == Enum.KeyCode[pickupKey] then
		if duplicate_preventer == true then
			if mouse.Target then
				if mouse.Target:FindFirstChild("Pickable") then
					local item = mouse.Target
					if item then
						local distanceFromItem = player:DistanceFromCharacter(item.Position)
						if distanceFromItem < 10 then
							Pickup_Event:FireServer(item)
							item:Destroy()
							duplicate_preventer = false

							for _, i in pairs(player.PlayerGui.Inventory_GUI.ScrollingFrame:GetDescendants()) do
								if i.Name == item.Name then
									i.Parent.Parent.Item_Count.Text = i.Parent.Parent.Item_Count.Text + 1
									duplicate_preventer = true
									break
								elseif i.Name == "None" then
									i.Name = item.Name
									i.Parent.Parent.Item_Name.Text = item.Name
									i.Parent.Parent.Item_Frame_Used.Text = "true"
									i.Parent.Parent.Item_Count.Text = 1
									duplicate_preventer = true
									break
								end
							end
						end
					end
				end
			end
		end
	end
end)
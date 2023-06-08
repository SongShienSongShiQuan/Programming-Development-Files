local UIS = game:GetService("UserInputService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Open_Cabinet_Event = ReplicatedStorage:WaitForChild("Open_Cabinet")
local Close_Cabinet_Event = ReplicatedStorage:WaitForChild("Close_Cabinet")
local open_key = "E"
local close_key = "F"

local player = game.Players.LocalPlayer
local mouse = player:GetMouse()
local duplicate_preventer = true
local PlayerGui = player:WaitForChild("PlayerGui")
local Open_GUI = PlayerGui:WaitForChild("Open_GUI")

UIS.InputChanged:Connect(function(input)
	if mouse.Target then
		if mouse.Target:FindFirstChild("Open_Enabled") then
			local target = mouse.Target
			Open_GUI.Adornee = target
			Open_GUI.ObjectName.Text = "Cabinet_1"
			Open_GUI.Enabled = true
			UIS.InputEnded:Connect(function(input)
				if input.KeyCode == Enum.KeyCode[open_key] and mouse.Target:FindFirstChild("Open_Enabled") then
					if duplicate_preventer == true then
						if mouse.Target:FindFirstChild("Open_Enabled") then
							local target = mouse.Target
							local target_Drawer = mouse.Target.Parent:FindFirstChild("Drawer_1")
							if target_Drawer then
								local distanceFromItem = player:DistanceFromCharacter(target.Position)
								if distanceFromItem < 20 then
									Open_Cabinet_Event:FireServer(target_Drawer)
									target_Drawer.Open.Enabled = true
									wait(1)
									target_Drawer.Open.Enabled = false
									print("Opening")
									local get_Item = target_Drawer:FindFirstChildWhichIsA("Part")
									get_Item.Transparency = 0
									local get_Bool = get_Item:FindFirstChildWhichIsA("BoolValue")
									get_Bool.Name = "Pickable"
								end
							end
						end
					end
				end
			end)
			UIS.InputEnded:Connect(function(input)
				if input.KeyCode == Enum.KeyCode[close_key] and mouse.Target:FindFirstChild("Open_Enabled") then
					if duplicate_preventer == true then
						if mouse.Target:FindFirstChild("Open_Enabled") then
							local target = mouse.Target
							local target_Drawer = mouse.Target.Parent:FindFirstChild("Drawer_1")
							if target_Drawer then
								local distanceFromItem = player:DistanceFromCharacter(target.Position)
								if distanceFromItem < 20 then
									Close_Cabinet_Event:FireServer(target_Drawer)
									target_Drawer.Close.Enabled = true
									wait(1)
									target_Drawer.Close.Enabled = false			
									print("Closing")
									local get_Item = target_Drawer:FindFirstChildWhichIsA("Part")
									get_Item.Transparency = 1
									local get_Bool = get_Item:FindFirstChildWhichIsA("BoolValue")
									get_Bool.Name = "Non_Pickable"
								end
							end
						end
					end
				end
			end)
		else
			Open_GUI.Adornee = nil
			Open_GUI.Enabled = false
		if mouse.Target:FindFirstChild("Open_Enabled_D2") then
			local target = mouse.Target
			Open_GUI.Adornee = target
			Open_GUI.ObjectName.Text = "Cabinet_2"
			Open_GUI.Enabled = true
			UIS.InputEnded:Connect(function(input)
				if input.KeyCode == Enum.KeyCode[open_key] and mouse.Target:FindFirstChild("Open_Enabled_D2") then
					if duplicate_preventer == true then
						if mouse.Target:FindFirstChild("Open_Enabled_D2") then
							local target = mouse.Target
							local target_Drawer = mouse.Target.Parent:FindFirstChild("Drawer_2")
							if target_Drawer then
								local distanceFromItem = player:DistanceFromCharacter(target.Position)
								if distanceFromItem < 20 then
									Open_Cabinet_Event:FireServer(target_Drawer)
									target_Drawer.Open.Enabled = true
									wait(1)
									target_Drawer.Open.Enabled = false
									print("Opening")
									local get_Item = target_Drawer:FindFirstChildWhichIsA("Part")
									get_Item.Transparency = 0
									local get_Bool = get_Item:FindFirstChildWhichIsA("BoolValue")
									get_Bool.Name = "Pickable"
								end
							end
						end
					end
				end
			end)
			UIS.InputEnded:Connect(function(input)
				if input.KeyCode == Enum.KeyCode[close_key] and mouse.Target:FindFirstChild("Open_Enabled_D2") then
					if duplicate_preventer == true then
						if mouse.Target:FindFirstChild("Open_Enabled_D2") then
							local target = mouse.Target
							local target_Drawer = mouse.Target.Parent:FindFirstChild("Drawer_2")
							if target_Drawer then
								local distanceFromItem = player:DistanceFromCharacter(target.Position)
								if distanceFromItem < 20 then
									Close_Cabinet_Event:FireServer(target_Drawer)
									target_Drawer.Close.Enabled = true
									wait(1)
									target_Drawer.Close.Enabled = false			
									print("Closing")
									local get_Item = target_Drawer:FindFirstChildWhichIsA("Part")
									get_Item.Transparency = 1
									local get_Bool = get_Item:FindFirstChildWhichIsA("BoolValue")
									get_Bool.Name = "Non_Pickable"
								end
							end
						end
					end
				end
			end)
		else
			Open_GUI.Adornee = nil
			Open_GUI.Enabled = false
		end
		end
	end
end)

local sec_a0001 = "Script section partition."
local sc_prt = script.Parent
local duplicate_preventer = true
local ammo_main = 6
local ammo_gui = script.Parent.Handle.BillboardGui.TextLabel
local ammo_int = sc_prt.Handle.Ammo.Value
local Revolver_sound = sc_prt.Handle["Revolver 38."]
local Revolver_Reload = sc_prt.Handle["Revolver Reload"]
local input_ = true
local runService = game:GetService("RunService")
local gun_f = require(script.Parent.Projectile.gun_projectile_f)
local UserInputService = game:GetService("UserInputService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Root_Part = sc_prt.Projectile.Root_Part
local VAL_L = sc_prt.VAL_L.Value.Position
local VAL_R = sc_prt.VAL_R.Value.Position

local GUN_FUNCTION_ENABLE_OR_DISABLE = true

local player = game.Players.LocalPlayer
local plr = player
local character_part = plr.Character
local mouse = plr:GetMouse()
local mouse_button_key_down = false

--Animation Variables.
local Reload_Anim_Var = game.Players.LocalPlayer.Character.Humanoid:LoadAnimation(sc_prt.Reload_Anim)
local animation1 = game.Players.LocalPlayer.Character.Humanoid:LoadAnimation(sc_prt.Animation1)
local animation2 = game.Players.LocalPlayer.Character.Humanoid:LoadAnimation(sc_prt.Animation2)
local animation3 = game.Players.LocalPlayer.Character.Humanoid:LoadAnimation(sc_prt.Animation3)

function activate_gun_f()
	gun_f.projectile()
end
local sec_a0002 = "Script section partition."
print("Reached 1.")
function On_Input(input)
	if GUN_FUNCTION_ENABLE_OR_DISABLE == true then
		if duplicate_preventer == true then
			if UserInputService:IsKeyDown(Enum.KeyCode.R) then
				local sec_a0003 = "Script section partition."
				print("Reached 4.")
				print(VAL_L)
				--local animation2 = game.Players.LocalPlayer.Character.Humanoid:LoadAnimation(sc_prt.Animation2)
				--animation2:Play()
				Reload_Anim_Var:Play()
				Revolver_Reload:Play()
				print("Reloading")
				duplicate_preventer = false
				--animation2:Play()
				ammo_main = 6
				ammo_gui.Text = ammo_main
				ammo_int = ammo_main
				wait(1)
				duplicate_preventer = true
				mouse_button_key_down = false
			end
		end
	end
end

mouse.Button1Down:connect(function()
	mouse_button_key_down = true
	if GUN_FUNCTION_ENABLE_OR_DISABLE == true then
		if duplicate_preventer == true then
			while mouse_button_key_down do
				local sec_a0004 = "Script section partition."
				animation3:Play()
				gun_f.projectile()				
				sc_prt.Barrel.Smoke.Enabled = true
				ammo_main = ammo_main - 1
				ammo_int = ammo_main
				ammo_gui.Text = ammo_main
				print(ammo_main)
				Revolver_sound:Play()
				duplicate_preventer = false
				wait(0.1)
				duplicate_preventer = true
				animation1:Play()
				sc_prt.Barrel.Smoke.Enabled = false
				if ammo_int < 1 then
					animation2:Play()
					Revolver_Reload:Play()
					print("Reloading")
					duplicate_preventer = false
					animation2:Play()
					ammo_main = 6
					ammo_int = ammo_main
					wait(1)
					duplicate_preventer = true
				end
			end
		end
	end
end)

mouse.Button1Up:connect(function()
	mouse_button_key_down = false
end)


--Equip & Unequip & UserInputService variables.
UserInputService.InputBegan:Connect(On_Input)
local ref_Walk = sc_prt.Walk_Loop
local sec_a0005 = "Script section partition."
sc_prt.Equipped:Connect(function()
	animation1:Play()
	local g_w = game.Workspace
	local get_player_VM_with_FPS_VM = sc_prt.Parent
	local Parent_Handle_Motor_6D = sc_prt.Parent.RightHand
	sc_prt.Handle.Handle_Motor_6D.Part0 = Parent_Handle_Motor_6D
	GUN_FUNCTION_ENABLE_OR_DISABLE = true
	for _, object in ipairs(g_w:GetChildren())  do
		if object.Name == get_player_VM_with_FPS_VM.Name then
			object.VM_with_FPS_VM.Enabled = true
			print("Equipped Gun.")
		end
	end
end)

sc_prt.Unequipped:Connect(function()
	local g_w = game.Workspace
	local get_player_VM_with_FPS_VM = sc_prt.Parent.Parent
	sc_prt.Handle.Handle_Motor_6D.Part0 = nil
	GUN_FUNCTION_ENABLE_OR_DISABLE = false
	for _, object in ipairs(g_w:GetChildren())  do
		if object.Name == get_player_VM_with_FPS_VM.Name then
			object.VM_with_FPS_VM.Enabled = false
			object.LeftarmWeld:Destroy()
			object.RightarmWeld:Destroy()
			print("Unequipped Gun.")
			local anim_idle = game.Players.LocalPlayer.Character.Humanoid:LoadAnimation(object.Animation_No_Tool)
			anim_idle:Play()
			animation1:Stop()
		end
	end
end)
local part = game.Workspace:FindFirstChild("DeathA")
local partA = game.Workspace:FindFirstChild("Anjing")

local sc = script.Parent 




local function ENABLEA()

	for key, value in pairs(workspace:GetDescendants()) do

		if value.Name == "DeathA" then
			value.actualscript.Disabled = false
		end
	end
end

local function DISABLEA()

	for key, value in pairs(workspace:GetDescendants()) do

		if value.Name == "DeathA" then
			value.actualscript.Disabled = true
		end
	end
end


local function ENABLEB()

	for key, value in pairs(workspace:GetDescendants()) do

		if value.Name == "DeathB" then
			value.actualscript.Disabled = false
		end
	end
end

local function DISABLEB()

	for key, value in pairs(workspace:GetDescendants()) do

		if value.Name == "DeathB" then
			value.actualscript.Disabled = true
		end
	end
end



local object = sc.VelocityFirstA
local printingvelocity = sc.SurfaceGui.Print

				local PosBR1a = workspace.Taft --Station Variables Engine Bodyposition.--
				local PosBR1b = workspace.Taft1

				local PosBR2a = workspace.Magallanes
				local PosBR2b = workspace.Magallanes1

				local bodyposB_TP = game.Workspace["MRT0-27 A2"]["Control B"].Main
				local bodyposA_TP = game.Workspace["MRT0-27 A2"].Control.Main

while true do
	wait(0.1)
	printingvelocity.Text = math.floor(object.Velocity.magnitude) --Floor Flat value, don't change..
		while math.floor(object.Velocity.magnitude) < 30 do wait(0.5) DISABLEA() DISABLEB()
	end
		while math.floor(object.Velocity.magnitude) > 30 do object.Beep:Play() wait(0.1) ENABLEA() ENABLEB() script.Parent.VelocityPrintA.Disabled = true wait(1) script.Parent.VelocityPrintA.Disabled = false
	end
end

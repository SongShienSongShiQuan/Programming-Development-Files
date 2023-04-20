local PosBR1a = workspace.TaftA --Station Variables Engine Bodyposition.--
local PosBR1b = workspace.Taft1A

local selectionA = game.Workspace["MRT0-27 A2"].A

	local PosBR2a = workspace.MagallanesA
	local PosBR2b = workspace.Magallanes1A

		local bodyposB = script.Parent["Control B"].Main.BodyPositionB
		local bodyposA = script.Parent.Control.Main.BodyPositionA
				local function GATE()
					for _, i in pairs(workspace["MRT0-27 A2"].Control:GetChildren()) do
				if i:IsA("MeshPart") then
				i.Transparency = 0.5
				end
			end
end

local function MotorsSound() --Local Functions call if needed this type of function.
	for _, i in pairs(selectionA:GetDescendants()) do
		if i:IsA("Sound") then
			i:Play()
			i.Volume = 0.5
			i.TimePosition = 0
		end
	end
end

local function MotorsSoundStop() --Local Functions call if needed this type of function.
	for _, i in pairs(selectionA:GetDescendants()) do
		if i:IsA("Sound") then
			wait(10)
			i.Volume = 0.1
		end
	end
end


while true do
	print("First")
		bodyposA.Position = PosBR2a.Position
		bodyposB.Position = PosBR2b.Position
	wait(60)
		bodyposA.Position = PosBR1a.Position
		bodyposB.Position = PosBR1b.Position
	wait(60)
	print("Hasilnya lumayan")
end
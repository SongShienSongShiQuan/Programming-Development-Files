local part = game.Workspace:FindFirstChild("DeathA")

local function onPartTouched(otherPart)
	-- Get the other part's parent
	local partParent = otherPart.Parent
	-- Look for a humanoid in the parent
	local humanoid = partParent:FindFirstChildWhichIsA("Humanoid")
	if humanoid then
		-- Do something to the humanoid, like set its health to 0
		humanoid.Health = 0
	end
end

part.Touched:Connect(onPartTouched)
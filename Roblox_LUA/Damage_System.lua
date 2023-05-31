local sc_prt = script.Parent
local damage_part = sc_prt
local function onPartTouched(otherPart)
	local partParent = otherPart.Parent
	local humanoid = partParent:FindFirstChildWhichIsA("Humanoid")
	if humanoid then
		humanoid.Health = 0
		local ReplicatedStorage = game:GetService("ReplicatedStorage")
		local remoteEvent = ReplicatedStorage:WaitForChild("Gun_Damage")

		-- Fire the RemoteEvent and pass additional arguments
		remoteEvent:FireServer(humanoid, Vector3.new(0, 25, 0))
		
	end
end
--do not enable, script is enabled with gun_projectile_f
damage_part.Touched:Connect(onPartTouched)
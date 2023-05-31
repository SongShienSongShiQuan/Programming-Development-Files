local Players = game:GetService("Players")

local coresChunk = script.Parent

local function onPartTouch(otherPart)
	local partParent = otherPart.Parent
	local humanoid = partParent:FindFirstChildWhichIsA("Humanoid")
	if humanoid then
		-- Destroy the pickup
		coresChunk:Destroy()
		-- Update the player's leaderboard stat
		local player = Players:GetPlayerFromCharacter(partParent)
		local leaderstats = player.leaderstats
		local accessplrgui = player.PlayerGui
		local coresStat = leaderstats and leaderstats:FindFirstChild("Cores")
		if coresStat then
			coresStat.Value = coresStat.Value + 10
			accessplrgui.MGUI.TotalCoreAmountsFrame.CoreAmount.Text = coresStat.Value
			local get_data = partParent.HumanoidRootPart.backpacktest.Test.DataValue
			get_data.Text = coresStat.Value
		end
	end
end
coresChunk.Touched:Connect(onPartTouch)
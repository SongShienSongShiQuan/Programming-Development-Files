game.Players.PlayerAdded:connect(function(player)
	player.CharacterAdded:connect(function(char)

		local torso = char:WaitForChild("HumanoidRootPart") --You can change this to another body part
		
		local ModelItem = game.ReplicatedStorage.backpacktest:Clone()
		ModelItem.Parent = torso

		local weldpart = Instance.new("Part", char)
		weldpart.Massless = true --You will likely want to set at least these properties
		weldpart.CanCollide = false
		weldpart.Anchored = false
		weldpart.Transparency = 1

		local weld = Instance.new("Weld", torso) --Could also use a Motor6D, or likewise
		weld.C0 = CFrame.new() --Both C0 and C1 are, by default, set to a blank CFrame
		weld.C1 = CFrame.new()
		weld.Part0 = torso
		weld.Part1 = weldpart
		
		local weld = Instance.new("Weld", torso) --Could also use a Motor6D, or likewise
		weld.C0 = CFrame.new() --Both C0 and C1 are, by default, set to a blank CFrame
		weld.C1 = CFrame.new()
		weld.Part0 = torso
		weld.Part1 = ModelItem

	end)
end)
local sc_prt = script.Parent

local input_ = true
local UserInputService = game:GetService("UserInputService")

UserInputService.InputBegan:Connect(function(input, gameProcessed)
	input_ = true
	while input_ == true do
		wait(1)
		if UserInputService:IsKeyDown(Enum.KeyCode.W) then
				print("Input!!")
			local animation4 = game.Players.LocalPlayer.Character.Humanoid:LoadAnimation(sc_prt.Animation4)
			animation4:Play()
		else
			input_ = false
		end
	end
end)
	

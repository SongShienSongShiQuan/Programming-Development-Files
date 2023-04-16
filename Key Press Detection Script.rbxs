--Key press detection script formula 

local userInputService = game:GetService("UserInputService")

userInputService.InputBegan:Connect(function(input, gameProcessedEven)
	
	print("Input Began") --Input began here, print for checking if it began--

	if input.UserInputType == Enum.UserInputType.Keyboard then

		if input.KeyCode == Enum.KeyCode.Q then
			print("Pressed letter Q")
		end
	end
end)
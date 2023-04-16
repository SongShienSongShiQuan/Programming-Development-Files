local SC = game.Workspace
local timeRemaining = 30

local boolmain = true

		while timeRemaining > 0 do
		script.Parent.Velocity = script.Parent.CFrame.LookVector* 30
			print("Low Speed")
			wait()
			timeRemaining = timeRemaining - 1
					wait()
			end
			local timeRemaining = timeRemaining +100
			
			while timeRemaining > 0 do
					script.Parent.Velocity = script.Parent.CFrame.LookVector* 80
					print("Medium Speed")
						wait()
						timeRemaining = timeRemaining - 1
	wait()
	end
	local timeRemaining = timeRemaining +150
	while timeRemaining > 0 do
			script.Parent.Velocity = script.Parent.CFrame.LookVector* 150
				print("High Speed")
				wait()
			timeRemaining = timeRemaining - 1
			wait()
		end
		local timeRemaining = timeRemaining +30
		while timeRemaining > 0 do
				script.Parent.Velocity = script.Parent.CFrame.LookVector* 500
							print("High Velocity")
							wait()
							timeRemaining = timeRemaining - 1
							wait()
		end
		local timeRemaining = timeRemaining +150
		while timeRemaining > 0 do
			script.Parent.Velocity = script.Parent.CFrame.LookVector* 1000
			print("High Speed")
			wait()
			timeRemaining = timeRemaining - 1
	           wait()
end
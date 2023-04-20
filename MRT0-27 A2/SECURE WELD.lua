local lock = false -->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>T6 WELD MAKE SURE TO ANCHOR FIRST!!!<<<<<<<<<<<<<<<<<<<<<< PLEASE READ
local directselect = game.Workspace["MRT0-27 A2"].A

local function SELECTNEXT() --Local Functions call if needed this type of function.
	for _, i in pairs(directselect:GetDescendants()) do
		if i:IsA("MeshPart") then
					print("Check, Error is 0 right now")
				
					lock = true print("Lock Initiated For Weld")

							local w = Instance.new("WeldConstraint")
								local sc = script.Parent
							local targetting = sc.Main
							w.Part0 = i w.Part1 = targetting w.Parent = i wait() 
						i.Anchored = false
						i.Anchored = false	
			end
		end
	end

local function SELECTNEXTA() --Local Functions call if needed this type of function.
	for _, i in pairs(directselect:GetDescendants()) do
		if i:IsA("Part") then
					print("Check, Error is 0 right now")

					lock = true print("Lock Initiated For Weld")

							local w = Instance.new("WeldConstraint")
							local sc = script.Parent
						local targetting = sc.Main
						w.Part0 = i w.Part1 = targetting w.Parent = i wait() 
					i.Anchored = false
			i.Anchored = false	
		end
	end
end

SELECTNEXTA()
SELECTNEXT()
			wait()
print("WeldFinish")		

		local endofscript = script.Parent

		endofscript["SECURE WELD"]:Destroy()



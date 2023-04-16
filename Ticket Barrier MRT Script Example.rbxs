--Ticket Barrier and for i formula

local start = script.Parent
local part = game.Workspace
local debounce = false
local function SELECTNEXT()
		for _, i in pairs(game.Workspace["TicketBarrierA-4B"].TicketBarrierB.DoorA:GetChildren()) do
		if i:IsA("Part") then
			i.Transparency = 0.5
			i.CanCollide = true
			debounce = true
		end
	end
end
		

local function SELECT()
		for _, i in pairs(game.Workspace["TicketBarrierA-4B"].TicketBarrierB.DoorA:GetChildren()) do
		if i:IsA("Part") then
			i.Transparency = 1
			i.CanCollide = false
			debounce = false
		end
	end
end
			
		

start.Touched:Connect(function(TOUCHINGPART)
	if TOUCHINGPART.Parent.Name == "HSRCard" then
		start.Beep:Play()
		part["TicketBarrierA-4B"].TicketBarrierB.MainPart.Denied.Transparency = 1
		part["TicketBarrierA-4B"].TicketBarrierB.MainPart.Granted.Transparency = 0
		SELECT()
		wait(2)
		part["TicketBarrierA-4B"].TicketBarrierB.MainPart.Denied.Transparency = 0
		part["TicketBarrierA-4B"].TicketBarrierB.MainPart.Granted.Transparency = 1
		SELECTNEXT()
	end
end)
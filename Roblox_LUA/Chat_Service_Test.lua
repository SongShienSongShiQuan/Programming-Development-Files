local ID = {75672459, 446469848} -- all userIds
local gw = game.Workspace
game.Players.PlayerAdded:Connect(function(Player)
	if table.find(ID, Player.UserId) then 
		Player.Chatted:Connect(function(msg)
			if string.lower(msg) == ":start" then
				print("Player said \":start\"")
				gw.ATT.Position = gw.Spawn_Location.ATT_Spawn_Main.Position
				gw.ALLIES.Position = gw.Spawn_Location.ALLIES_Spawn_Main.Position
				gw.OPPS.Position = gw.Spawn_Location.OPPS_Spawn_Main.Position
			else if string.lower(msg) == ":reset" then
				print("Player said \":reset\"")
				gw.ATT.Position = gw.Spawn_Location.ATT_Spawn_Lobby.Position
				gw.ALLIES.Position = gw.Spawn_Location.ALLIES_Spawn_Lobby.Position
				gw.OPPS.Position = gw.Spawn_Location.OPPS_Spawn_Lobby.Position
				end
			end
		end)
	end
end)
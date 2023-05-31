game.Players.PlayerAdded:connect(function(player)
	player.CharacterAdded:connect(function(char)
		local DataStoreService = game:GetService('DataStoreService')
		local playerData = DataStoreService:GetDataStore('PlayerData')
		local Players = game:GetService("Players")
		local playerDataWood = DataStoreService:GetDataStore('PlayerDataWood')
		local playerDataLeaves = DataStoreService:GetDataStore('PlayerDataLeaves')
		
				local playerUserId = 'Player_'..player.UserId
				local data = playerData:GetAsync(playerUserId)
		
				local playerUserId = 'Player_'..player.UserId
				local data = playerData:GetAsync(playerUserId)

				local playerUserId = 'Player_'..player.UserId
				local dataLeaves = playerDataLeaves:GetAsync(playerUserId)

				local playerUserId = 'Player_'..player.UserId
				local dataWood = playerDataWood:GetAsync(playerUserId)
		
				local torso = char:WaitForChild("HumanoidRootPart")
				wait(2)
		torso.backpacktest.Test.DataValue.Text = data
		print("Successful Sync")
	end)
end)
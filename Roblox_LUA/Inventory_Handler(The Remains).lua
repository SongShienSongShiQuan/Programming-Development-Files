local ReplicatedStorage = game:GetService("ReplicatedStorage")
local DropItem = ReplicatedStorage:WaitForChild("DropItem")
local sc_prt = script.Parent
local player = sc_prt.Parent.Parent.Parent.Parent
local Button = sc_prt.ImageButton
wait(sc_prt.Wait_Int.Text)
sc_prt.Wait_Int.Text = 0
local leaderstats = player.leaderstats
local accessplrgui = player.PlayerGui
local Item_Name = sc_prt.Item_Name:FindFirstChildWhichIsA("TextLabel")
local get_Item_Name = Item_Name.Name
local Item_Stats = player.Item_Inventory:FindFirstChild(get_Item_Name)
Button.MouseButton2Up:Connect(function()
	if Item_Stats.Value > 0 then
		sc_prt.Item_Name.Text = get_Item_Name
		sc_prt.Item_Count.Text = sc_prt.Item_Count.Text - 1	
		sc_prt.Item_Frame_Used.Text = "true"
		if Item_Stats then
			Item_Stats.Value = Item_Stats.Value - 1
			DropItem:FireServer(Item_Stats)
	if Item_Stats.Value <= 0 then
		sc_prt.Item_Name.Text = " "
		sc_prt.Item_Frame_Used.Text = "false"
		sc_prt.Item_Count.Text = " "
		local Get_Item_None_Name = sc_prt.Item_Name:FindFirstChildWhichIsA("TextLabel")
		Get_Item_None_Name.Name = "None"
	end
	end
	end
end)
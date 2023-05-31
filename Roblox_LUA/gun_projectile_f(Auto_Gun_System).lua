local gun_f = {}
function gun_f.projectile()
	local sc_prt = script.Parent


	local player = game.Players.LocalPlayer
	local mouse = player:GetMouse()
	local projectile = sc_prt.Parent.Projectile.Projectile_SMG:Clone()
	projectile.Damage_System.Enabled = true
	print(projectile.Damage_System.Enabled)
	projectile.WeldConstraint:Destroy()
	projectile.CanCollide = false
	projectile.Transparency = 0
	projectile.Name = "Bullet_1"
	projectile.CFrame = sc_prt.Root_Part.CFrame * CFrame.new(0,0,-2)
	projectile.Size = Vector3.new(1,1,1)
	projectile.Material = "Neon"
	projectile.Massless = true
	projectile.CFrame = CFrame.new(projectile.Position, mouse.Hit.p)
	projectile.Parent = sc_prt

	local antiGravity = Instance.new("BodyForce")
	antiGravity.Force = Vector3.new(0, workspace.Gravity * projectile:GetMass(), 0)
	antiGravity.Parent = projectile

	projectile.Velocity = CFrame.new(player.Character.HumanoidRootPart.Position, mouse.Hit.p).lookVector * 100 -- change this number to a smaller number if you want the bullet to go slower


		print("gun_f got executed...")
		game.Debris:AddItem(projectile, 1) -- (projectile, >>int_val<<) add int val inside ex: (projectile , 1). Do not add >><<.
		projectile.Touched:Connect(function()
		antiGravity:Destroy()
	end)
end
return gun_f

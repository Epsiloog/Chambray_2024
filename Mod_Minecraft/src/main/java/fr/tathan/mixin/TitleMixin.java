package fr.tathan.mixin;

import net.minecraft.client.Minecraft;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Overwrite;

/**
 *
 * Une classe qui permet de modifier le code du jeu et changer le titre de la fenetre. A referencer dans le fichier modid.mixins.json
 *
 **/

@Mixin(Minecraft.class)
public class TitleMixin {

	@Overwrite
	private String createTitle() {
		return "Telligo ! Ambre la mechante ! Vive le CCL et le NFO !";
	}
}
package fr.tathan;

import fr.tathan.common.events.Events;
import fr.tathan.common.registry.BlocksRegistry;
import fr.tathan.common.registry.GameRuleRegistry;
import fr.tathan.common.registry.GenRegistry;
import fr.tathan.common.registry.ItemsRegistry;
import net.fabricmc.api.ClientModInitializer;
import net.fabricmc.api.ModInitializer;

import net.minecraft.client.Minecraft;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 *
 * La class principale du Mod. On Initialise toutes nos class qui register des items
 * A referencer dans le fichier fabric.mod.json
 *
 *
 *
 * Le mod contient aussi un fichier assets, qui prend en compte tout les fichiers pour le models des items/blocks, les textures et lang
 * Le mod contient aussi un fichier data, qui prend en compte tout les features, tags, etc...
 **/
public class TelluckyBlock implements ModInitializer {

    public static final Logger LOGGER = LoggerFactory.getLogger("tellucky-block");

	/** Le MODID qui est l'identifiant du mod **/
	public static final String MODID = "tellucky-block";


	/** **/
	@Override
	public void onInitialize() {

		LOGGER.info("Hello Fabric world!");
		ItemsRegistry.initialize();
		BlocksRegistry.initialize();
		GameRuleRegistry.initialize();
		Events.init();
		GenRegistry.init();
	}

}
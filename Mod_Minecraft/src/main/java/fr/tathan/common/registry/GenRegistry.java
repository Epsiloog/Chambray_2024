package fr.tathan.common.registry;

import fr.tathan.TelluckyBlock;
import net.fabricmc.fabric.api.biome.v1.BiomeModifications;
import net.fabricmc.fabric.api.biome.v1.BiomeSelectors;
import net.minecraft.core.Registry;
import net.minecraft.data.BuiltinRegistries;
import net.minecraft.resources.ResourceKey;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.level.levelgen.GenerationStep;

public class GenRegistry {

    /** On utilise une method de Fabric, le modloader, pour ajouter des feature lors de la generation du monde **/
    public static void init() {

        BiomeModifications.addFeature(
                BiomeSelectors.foundInOverworld(),
                // the feature is to be added while flowers and trees are being generated
                GenerationStep.Decoration.VEGETAL_DECORATION,
                ResourceKey.create(Registry.PLACED_FEATURE_REGISTRY, new ResourceLocation(TelluckyBlock.MODID, "lucky_spawn")));
    }

}

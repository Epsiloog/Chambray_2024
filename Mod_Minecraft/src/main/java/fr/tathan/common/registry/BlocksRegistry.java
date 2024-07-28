package fr.tathan.common.registry;

import fr.tathan.TelluckyBlock;
import fr.tathan.common.blocks.LuckyBlock;
import net.minecraft.core.Registry;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.material.Material;
import net.minecraft.world.level.material.MaterialColor;

public class BlocksRegistry {


    /** On register un Block avec notre methode
     *
     * On utilise notre class custom puis un ID custom pour qu'on puisse recup le block après
     *
     **/
    public static final Block TELLUCKY_BLOCK = register(
            // Ignore the food component for now, we'll cover it later in the food section.
            new LuckyBlock(BlockBehaviour.Properties.of(Material.DIRT, MaterialColor.COLOR_YELLOW)),
            "tellucky_block"
    );


    /** Une méthode qui permet d'ajouter notre block dans la liste des blocks de Minecraft **/
    public static Block register(Block block, String id) {
        ResourceLocation itemID = new ResourceLocation(TelluckyBlock.MODID, id);
        Block registeredBlock = Registry.register(Registry.BLOCK, itemID, block);
        return registeredBlock;
    }


    /** Method pour initialisé les blocks **/
    public static void initialize() {
    }

}

package fr.tathan.common.events;

import fr.tathan.TelluckyBlock;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerLifecycleEvents;
import net.fabricmc.fabric.api.event.player.AttackEntityCallback;
import net.fabricmc.fabric.api.event.server.ServerStartCallback;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.entity.player.Player;

import static fr.tathan.common.registry.GameRuleRegistry.SHOULD_PLAYER_ATTACK;

public class Events {

    /** Une méthode pour mettre tout nos Events **/
    public static void init() {

        /** Une event qui est appelé quand un JOueur tape une entité **/

        AttackEntityCallback.EVENT.register((player, world, hand, entity, hitResult) -> {
            if (world.isClientSide) return InteractionResult.PASS;
            if (entity instanceof Player playerAttacked) {

                if (!world.getGameRules().getRule(SHOULD_PLAYER_ATTACK).get()) {
                    playerAttacked.heal(2000);
                    return InteractionResult.FAIL;
                }
            }

            return InteractionResult.PASS;

        });

        /** Une event qui est appelé quand le serveur s'active **/
        ServerLifecycleEvents.SERVER_STARTED.register( (server -> {
            TelluckyBlock.LOGGER.info("WorldBorder Set");
            server.overworld().getWorldBorder().setCenter(0, 0);
            server.overworld().getWorldBorder().setSize(800);

        }));
    }

}
